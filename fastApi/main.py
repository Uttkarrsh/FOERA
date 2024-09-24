from fastapi import FastAPI, Depends, HTTPException, status, Path, Body
from typing import List
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from auth import hash_password, verify_password, create_access_token, decode_access_token
from models import User, Products, Wishlist, Cart, Address, Order, OrderItem
from datetime import datetime
from schema import UserCreate, UserResponse, UserLogin, Token, ProductCreate, ProductResponse, WishlistItemResponse, CartItemCreate,CartItemResponse, CheckoutResponse, AddressCreate, AddressResponse, OrderResponse


app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/signup", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == user.name).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    db_user = User(
        name=user.name,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == user.name).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid name or password")
    
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid name or password")
    
    access_token = create_access_token(data={"sub": db_user.name})
    return {"access_token": access_token, "token_type": "bearer", "user_id":db_user.id, "user_name":db_user.name}





@app.post("/add-products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Products(
        name=product.name,
        category=product.category,
        description=product.description,
        image=product.image
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/{category}" ,response_model=list[ProductResponse])
def get_by_category(category: str, db: Session = Depends(get_db)):
    products = db.query(Products).filter(Products.category == category).all()
    return products


@app.get("/products", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Products).all()
    return products

@app.post("/user/{user_id}/wishlist/{product_id}", status_code=201)
def add_to_wishlist(user_id: int = Path(..., title="User ID"), product_id: int = Path(..., title="Product ID"), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    product = db.query(Products).filter(Products.id == product_id).first()
    if not product:
        raise HTTPException(status_code=401, detail="Product not found")
    
    wishlist_item = Wishlist(user_id=user_id, product_id=product_id)
    db.add(wishlist_item)
    db.commit()
    db.refresh(wishlist_item)
    return {"message": f"Product {product_id} added to wishlist for user {user_id}"}

@app.get("/user/{user_id}/wishlist", response_model=List[WishlistItemResponse])
def get_wishlist(user_id: int, db: Session = Depends(get_db)):
  
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    wishlist_items = db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
    return wishlist_items


@app.post("/user/{user_id}/cart/{product_id}", status_code=201)
def add_to_cart(user_id: int = Path(..., title="User ID"), product_id: int = Path(..., title="Product ID"), cart_item: CartItemCreate = Body(...), db: Session = Depends(get_db)):    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    product = db.query(Products).filter(Products.id == product_id).first()
    if not product:
        raise HTTPException(status_code=401, detail="Product not found")
    
    cart_item_db = Cart(
        user_id=user_id,
        product_id=product_id,
        quantity=cart_item.quantity,
        created_at=datetime.utcnow()
    )
    db.add(cart_item_db)
    db.commit()
    db.refresh(cart_item_db)
    return cart_item_db

@app.get("/user/{user_id}/cart", response_model=List[CartItemResponse])
def get_cart_items(user_id: int, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    return cart_items

@app.delete("/user/{user_id}/cart/{product_id}", status_code=204)
def remove_from_cart(user_id: int = Path(..., title="User ID"), product_id: int = Path(..., title="Product ID"), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cart_item = db.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == product_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Product not found in cart")

    db.delete(cart_item)
    db.commit()

    return {"detail": "Product removed from cart successfully"}



@app.get("/category/{category_name}", response_model=List[ProductResponse])
def get_products_by_category(category_name: str, db: Session = Depends(get_db)):
    products = db.query(Products).filter(Products.category == category_name).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found in this category")
    return products


@app.get("/user/{user_id}/checkout", response_model=CheckoutResponse)
def get_checkout(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()

    total_cost = 0.0
    cart_items_response = []

    for item in cart_items:
        product = db.query(Products).filter(Products.id == item.product_id).first()
        total_cost += item.quantity * product.cost
        cart_items_response.append(CartItemResponse(
            id=item.id,
            quantity=item.quantity,
            user_id=item.user_id,
            created_at=item.created_at,
            product=ProductResponse(
                id=product.id,
                name=product.name,
                category=product.category,
                image=product.image,
                created_at=product.created_at,
                cost=product.cost
            )
        ))

    latest_order = db.query(Order).filter(Order.user_id == user_id).order_by(Order.created_at.desc()).first()
    order_id = latest_order.id if latest_order else None

    return CheckoutResponse(
        order_id=order_id,
        cart_items=cart_items_response,
        total_cost=total_cost
    )



@app.post("/user/{user_id}/address", response_model=AddressResponse)
def create_address(user_id: int, address: AddressCreate, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_address = Address(
        address_line1=address.address_line1,
        address_line2=address.address_line2,
        city=address.city,
        state=address.state,
        pincode=address.pincode,
        user_id=user_id
    )
    
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    
    return new_address

@app.post("/user/{user_id}/checkout", response_model=CheckoutResponse)
def checkout(user_id: int, db: Session = Depends(get_db)):
    # Step 1: Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Step 2: Get all cart items for the user
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # Step 3: Ensure user has an address
    address = db.query(Address).filter(Address.user_id == user_id).first()
    if not address:
        raise HTTPException(status_code=400, detail="No address found. Add an address before checkout.")

    # Step 4: Calculate total cost
    total_cost = 0.0
    cart_items_response = []

    for item in cart_items:
        product = db.query(Products).filter(Products.id == item.product_id).first()
        total_cost += item.quantity * product.cost

        # Create a cart item response for each product
        cart_items_response.append(CartItemResponse(
            id=item.id,
            quantity=item.quantity,
            user_id=item.user_id,
            created_at=item.created_at,
            product=ProductResponse(
                id=product.id,
                name=product.name,
                category=product.category,
                image=product.image,
                created_at=product.created_at,
                cost=product.cost
            )
        ))

    # Step 5: Create an Order
    order = Order(user_id=user_id, total_cost=total_cost)
    db.add(order)
    db.commit()
    db.refresh(order)

    # Step 6: Create Order Items
    for item in cart_items:
        product = db.query(Products).filter(Products.id == item.product_id).first()
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=item.quantity,
            total_price=item.quantity * product.cost
        )
        db.add(order_item)

    db.commit()

    # Step 7: Clear the user's cart
    # db.query(Cart).filter(Cart.user_id == user_id).delete()
    # db.commit()

    # Step 8: Return checkout response
    return CheckoutResponse(
        order_id=order.id,
        cart_items=cart_items_response,
        total_cost=total_cost
    )


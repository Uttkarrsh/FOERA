import React, { useState } from "react";
import { Link } from "react-router-dom";
import ParticleBackground from "./particle";

function Login() {
  const [username, setMobileNumber] = useState("");
  const [password, setPassword] = useState("");
  return (
    <>
      <div className="relative h-screen w-screen overflow-hidden">
        <div className="absolute inset-0 z-0">
          <ParticleBackground />
        </div>
        <div className="absolute inset-0 flex items-center justify-center mx-10 z-10">
          <div className="space-y-4 w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0  dark:border-gray-700">
            <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 className="text-xl font-bold leading-tight text-darkPink tracking-tight text-gray-900 md:text-4xl">
                FOERA
              </h1>
              <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl">
                Sign in to your account
              </h1>
              <form className="space-y-4 md:space-y-6" action="#">
                <div>
                  <label
                    for="email"
                    className="block mb-2 text-sm font-medium text-gray-900"
                  >
                    Your email or Mobile Number
                  </label>
                  <input
                    type="text"
                    name="email"
                    id="email"
                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 
                                focus:border-primary-600 block w-full p-2.5 dark:border-gray-600 dark:placeholder-gray-400  dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Mobile number or Email"
                    required=""
                    onChange={(e) => {
                      setMobileNumber(e.target.value);
                    }}
                  />
                </div>
                <div>
                  <label
                    for="password"
                    className="block mb-2 text-sm font-medium text-gray-900"
                  >
                    Password
                  </label>
                  <input
                    type="password"
                    name="password"
                    id="password"
                    placeholder="••••••••"
                    className="bg-gray-50 border border-gray-300 
                                text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:border-gray-600 dark:placeholder-gray-400
                                dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    required=""
                    onChange={(e) => {
                      setPassword(e.target.value);
                    }}
                  />
                </div>
                <div className="flex items-center justify-between"></div>
                <button
                  type="button"
                  className="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 
                            text-center dark:bg-darkPink dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                >
                  Sign in
                </button>
                {/* <button type="button" className="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 
                            text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" onClick={logout}>Sign in</button> */}
                {/* <p>{message}</p> */}
                <div>
                  <p className="block mb-2 text-sm font-medium text-gray-900 ">
                    Don't have an account?
                  </p>
                  <div className="flex justify-between">
                    <Link to="/signup">
                      <p className="block mb-2 text-sm font-medium text-gray-900 ">
                        Sign Up
                      </p>
                    </Link>
                    {/* <Link to="/change-password">
                      <p className="block mb-2 text-sm font-medium text-gray-900 ">
                        Forgot Password?
                      </p>
                    </Link> */}
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Login;

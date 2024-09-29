import React from "react";
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";

function Particle() {
  const particlesInit = async (main) => {
    console.log(main);
    await loadFull(main);
  };

  const particlesLoaded = (container) => {
    console.log(container);
  };

  return (
    <Particles
      id="tsparticles"
      init={particlesInit}
      loaded={particlesLoaded}
      options={{
        background: {
          color: "#75484D",
        },
        fpsLimit: 120,
        interactivity: {
          detectsOn: "canvas",
          events: {
            onHover: {
              enable: true,
              mode: "repulse",
            },
            onClick: {
              enable: true,
              mode: "push",
            },
            resize: true,
          },
          modes: {
            repulse: {
              distance: 100,
              duration: 0.4,
            },
            push: {
              quantity: 4,
            },
          },
        },
        particles: {
          shape: {
            type: ["circle", "polygon"], // Array of shapes
            polygon: {
              nb_sides: 5, // Number of sides for the polygon particles
            },
          },
          size: {
            random: {
              enable: true,
              minimumValue: 0.5,
            },
            value: 8.0,
          },
          color: {
            value: ["#DDACB1", "#E3C2C1"], // Array of colors
          },
          number: {
            density: {
              enable: true,
              area: 1080,
            },
            limit: 0,
            value: 300,
          },
          opacity: {
            animation: {
              enable: true,
              minimumValue: 0.5,
              speed: 1.6,
              sync: false,
            },
            random: {
              enable: true,
              minimumValue: 0.1,
            },
            value: 1,
          },
          move: {
            enable: true,
            speed: 2,
            direction: "none",
            random: false,
            straight: false,
            outModes: {
              default: "bounce",
            },
            attract: {
              enable: false,
              rotateX: 600,
              rotateY: 1200,
            },
          },
        },
      }}
    />
  );
}

export default Particle;

<template>
  <div class="blob">
    <svg width="900" height="900" viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(300,300)">
        <path
          d="M105.9,-139.7C148.7,-114.6,202.7,-99,218,-67.2C233.3,-35.4,209.9,12.6,180.3,44.7C150.7,76.8,115,93,84,120.4C52.9,147.8,26.5,186.4,-6.4,195.2C-39.2,203.9,-78.4,182.9,-107.4,154.8C-136.4,126.7,-155.2,91.6,-158.6,57.2C-162,22.8,-149.9,-11,-143.1,-50.9C-136.2,-90.8,-134.5,-136.8,-111.5,-168.4C-88.6,-199.9,-44.3,-216.9,-6.4,-208.2C31.5,-199.4,63.1,-164.8,105.9,-139.7Z"
        />
      </g>
    </svg>
  </div>
</template>

<style lang="scss">
@-webkit-keyframes organic {
  0% {
    -webkit-transform: scale(0.9, 0.9) rotate(0);
    transform: scale(0.9, 0.9) rotate(0);
  }
  20% {
    -webkit-transform: scale(0.9, 0.8) rotate(-10deg);
    transform: scale(0.9, 0.8) rotate(-10deg);
  }
  40% {
    -webkit-transform: scale(0.8, 1) rotate(-30deg);
    transform: scale(0.8, 1) rotate(-30deg);
  }
  60% {
    -webkit-transform: scale(0.7, 0.9) rotate(-10deg);
    transform: scale(0.7, 0.9) rotate(-10deg);
  }
  80% {
    -webkit-transform: scale(0.9, 0.8) rotate(10deg);
    transform: scale(0.9, 0.8) rotate(10deg);
  }
  100% {
    -webkit-transform: scale(0.9, 0.9) rotate(0);
    transform: scale(0.9, 0.9) rotate(0);
  }
}
@keyframes organic {
  0% {
    -webkit-transform: scale(0.9, 0.9) rotate(0);
    transform: scale(0.9, 0.9) rotate(0);
  }
  20% {
    -webkit-transform: scale(0.9, 0.8) rotate(-10deg);
    transform: scale(0.9, 0.8) rotate(-10deg);
  }
  40% {
    -webkit-transform: scale(0.8, 1) rotate(-30deg);
    transform: scale(0.8, 1) rotate(-30deg);
  }
  60% {
    -webkit-transform: scale(0.7, 0.9) rotate(-10deg);
    transform: scale(0.7, 0.9) rotate(-10deg);
  }
  80% {
    -webkit-transform: scale(0.9, 0.8) rotate(10deg);
    transform: scale(0.9, 0.8) rotate(10deg);
  }
  100% {
    -webkit-transform: scale(0.9, 0.9) rotate(0);
    transform: scale(0.9, 0.9) rotate(0);
  }
}

.blob {
  position: fixed;
  right: -5vw;
  top: 1vh;
  width: auto;
  height: auto;
  z-index: -1;

  svg {
    fill: rgba(#8487c2, 0.1);

    path {
      -webkit-animation-name: organic;
      animation-name: organic;
      -webkit-animation-duration: 20s;
      animation-duration: 20s;
      -webkit-animation-iteration-count: infinite;
      animation-iteration-count: infinite;
      -webkit-animation-timing-function: linear;
      animation-timing-function: linear;
      -webkit-transform-origin: center;
      transform-origin: center;
    }
  }
}
</style>
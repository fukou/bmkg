<template>
  <div>
    <NavBar />
    <div class="container">
      <transition name="fade">
        <nuxt />
      </transition>
    </div>
    <Blob />
  </div>
</template>

<script>
import NavBar from '../components/NavBar'
import Blob from '~/components/Blob'

export default {
  components: {
    NavBar,
    Blob
  }
}
</script>

<style lang="scss">
@import '../assets/styles/reset';

@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Regular.woff2') format('woff2'),
    url('/fonts/Inter-Regular.woff') format('woff');
}

@font-face {
  font-family: 'Inter';
  font-weight: 600;
  src: url('/fonts/Inter-Bold.woff2') format('woff2'),
    url('/fonts/Inter-Bold.woff') format('woff');
}

@font-face {
  font-family: 'Inter';
  font-weight: 800;
  src: url('/fonts/Inter-ExtraBold.woff2') format('woff2'),
    url('/fonts/Inter-ExtraBold.woff') format('woff');
}

body {
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
}

html {
  line-height: 1.35;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}

.container {
  margin: 10rem auto;
  padding: 0 2rem;
  max-width: 60rem;

  @media (max-width: 60rem) {
    margin: 7.5rem auto;
  }

  h1 {
    margin-bottom: 1rem;
    font-size: 1.65em;
    font-weight: 600;

    @media (max-width: 40rem) {
      font-size: 1.3em;
    }
  }

  .logo {
    max-width: 90px;
    margin: 0 auto 1.85rem auto;

    @media (max-width: 40rem) {
      max-width: 70px;
    }
  }

  p {
    margin: auto;
    max-width: 50%;
    color: #777;
    font-size: 1.05em;
    font-family: 'Lato', 'Inter', Arial, Helvetica, sans-serif;

    @media (max-width: 60rem) {
      max-width: 100%;
    }
  }

  &__inner {
    text-align: center;
  }
}

// .fade-enter-active,
// .fade-leave-active {
//   transition: opacity 0.65s;
// }
// .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
//   opacity: 0;
// }

::-moz-selection {
  color: #111;
  background: rgb(252, 252, 167);
}

::selection {
  color: #111;
  background: rgb(252, 252, 167);
}
</style>

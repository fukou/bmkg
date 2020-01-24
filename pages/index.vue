<template>
  <div>
    <div class="container__inner">
      <img class="logo" src="~/assets/images/logo.png" alt="Logo BMKG" />
      <h1>Aplikasi Prediksi Banjir BMKG Cilacap</h1>
      <p>Gunakan pencarian di bawah ini untuk memprediksi banjir setelah tahun 2010 dengan memilih tanggal dan tahun.</p>
      <Search />
    </div>
  </div>
</template>

<script>
// import Grid from '../components/Grid'
import Search from '~/components/Search'
export default {
  components: {
    Search
  },
  mounted() {
    // if (process.client) {
    //   this.$scrollTo('body', 0, { force: true })
    // }

    window.scrollTo(0, 0)
  },
  head() {
    return {
      title: 'Aplikasi Prediksi Banjir BMKG Cilacap'
    }
  }
}
</script>
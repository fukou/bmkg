<template>
  <div>
    <div class="about">
      <h1>Tentang kami</h1>Aplikasi website ini dibuat untuk memprediksi banjir dengan memperhatikan tingkat curah hujan. Berikut indikator jumlah curah hujan
    </div>
    <Grid />
  </div>
</template>

<script>
import Grid from '~/components/Grid'

export default {
  components: {
    Grid
  },
  head() {
    return {
      title: 'Tentang kami | Aplikasi Prediksi Banjir BMKG Cilacap'
    }
  },
  mounted() {
    // if (process.client) {
    //   this.$scrollTo('body', 0, { force: true })
    // }
    window.scrollTo(0, 0)
  }
}
</script>

<style lang="scss" scoped>
.about {
  color: #777;
  font-size: 1.05em;
  font-family: 'Lato', 'Inter', Arial, Helvetica, sans-serif;

  i,
  em {
    font-weight: bold;
    color: #555;
  }

  h1 {
    color: #111;
    font-family: 'Inter', sans-serif;
  }
}
</style>
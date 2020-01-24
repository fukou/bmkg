<template>
  <div class="grid__p">
    <div class="grid__p--content">
      <h2>Rendah</h2>
      <ul>
        <li>0 – 20 mm</li>
        <li>21 – 50 mm</li>
        <li>51 – 100 mm</li>
      </ul>
    </div>
    <div class="grid__p--content">
      <h2>Menengah</h2>
      <ul>
        <li>101 mm – 150 mm</li>
        <li>150 mm – 200 mm</li>
        <li>201 mm – 300 mm</li>
      </ul>
    </div>
    <div class="grid__p--content">
      <h2>Tinggi</h2>
      <ul>
        <li>301 mm – 400 mm</li>
        <li>401 mm – 500 mm</li>
      </ul>
    </div>
    <div class="grid__p--content">
      <h2>Sangat Tinggi</h2>
      <ul>
        <li>Lebih dari 500 mm</li>
      </ul>
    </div>
  </div>
</template>

<style lang="scss">
.grid__p {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2.5rem;
  margin-top: 3.5rem;

  @media (max-width: 60rem) {
    grid-template-columns: 1fr;
    grid-gap: 1.25rem;
  }

  & > &--content {
    border: 1px solid #ddd;
    background-color: #fff;
    padding: 2.5rem 2.5rem;
    -webkit-border-radius: 13px;
    border-radius: 13px;

    -webkit-transition: 0.5s;
    -moz-transition: 0.5s;
    transition: 0.5s;

    &:hover {
      transform: translateY(-5%);
      box-shadow: 4px 8px 14px rgba(0, 0, 0, 0.07);
    }

    h2 {
      @media (max-width: 40rem) {
        font-size: 1.3em;
      }
    }

    ul {
      text-align: left;
      list-style: none;
      margin: 0;
      padding: 0;
      margin-top: 1rem;
    }

    .btn-go {
      font-family: inherit;
      font-size: 0.9em;
      display: block;
      cursor: pointer;
      margin: 1rem auto 0 auto;
      background-color: #8487c2;
      padding: 0.65rem 1.5rem;
      color: #fff;
      border: 0;
      -moz-border-radius: 30px;
      -webkit-border-radius: 30px;
      border-radius: 30px;

      -webkit-transition: 0.5s;
      -moz-transition: 0.5s;
      transition: 0.5s;

      &:hover {
        background-color: #111;
      }
    }
  }
}
</style>
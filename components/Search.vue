<template>
  <div class="prediction">
    <input
      type="text"
      class="prediction__input"
      name="prediction"
      placeholder="Masukkan tanggal dan tahun disini..."
    />
    <button class="prediction__button">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
        <path
          d="M443.5 420.2L336.7 312.4c20.9-26.2 33.5-59.4 33.5-95.5 0-84.5-68.5-153-153.1-153S64 132.5 64 217s68.5 153 153.1 153c36.6 0 70.1-12.8 96.5-34.2l106.1 107.1c3.2 3.4 7.6 5.1 11.9 5.1 4.1 0 8.2-1.5 11.3-4.5 6.6-6.3 6.8-16.7.6-23.3zm-226.4-83.1c-32.1 0-62.3-12.5-85-35.2-22.7-22.7-35.2-52.9-35.2-84.9 0-32.1 12.5-62.3 35.2-84.9 22.7-22.7 52.9-35.2 85-35.2s62.3 12.5 85 35.2c22.7 22.7 35.2 52.9 35.2 84.9 0 32.1-12.5 62.3-35.2 84.9-22.7 22.7-52.9 35.2-85 35.2z"
        />
      </svg>
      <span class="text__input">Mulai prediksi</span>
    </button>
  </div>
</template>

<style lang="scss" scoped>
.prediction {
  display: flex;
  align-items: center;
  margin: 3rem auto;
  padding: 0.5rem 0.85rem;
  width: 80%;
  mix-blend-mode: normal;
  border: 1px solid #cccccc;
  background-color: #fff;
  box-sizing: border-box;
  box-shadow: 0px 3.68045px 5.34081px rgba(0, 0, 0, 0.0196802),
    0px 8.84464px 12.8347px rgba(0, 0, 0, 0.0282725),
    0px 16.6537px 24.1666px rgba(0, 0, 0, 0.035),
    0px 29.7073px 43.1091px rgba(0, 0, 0, 0.0417275),
    0px 55.5642px 80.6308px rgba(0, 0, 0, 0.0503198),
    0px 133px 193px rgba(0, 0, 0, 0.07);
  border-radius: 100px;
  transition: 0.5s;
  font-family: 'Lato', sans-serif;

  @media (min-width: 60rem) {
    &:focus,
    &:focus-within {
      border: 1px solid #8487c2;
    }
  }

  &__input {
    flex: 1 0 auto;
    padding: 0 1rem;
    border: 1px solid transparent;

    @media (max-width: 60rem) {
      width: 100%;
      padding: 0.95rem 1.25rem;
      font-size: 0.85em;
      border: 1px solid #cccccc;
      background-color: #fff;
      box-sizing: border-box;
      box-shadow: 0px 3.68045px 5.34081px rgba(0, 0, 0, 0.0196802),
        0px 8.84464px 12.8347px rgba(0, 0, 0, 0.0282725),
        0px 16.6537px 24.1666px rgba(0, 0, 0, 0.035),
        0px 29.7073px 43.1091px rgba(0, 0, 0, 0.0417275),
        0px 55.5642px 80.6308px rgba(0, 0, 0, 0.0503198),
        0px 133px 193px rgba(0, 0, 0, 0.07);
      border-radius: 100px;
    }
  }

  &__button {
    cursor: pointer;
    width: 46px;
    height: 46px;
    background: #8487c2;
    border-radius: 100px;
    border: 1px solid transparent;

    @media (max-width: 60rem) {
      width: 100%;
      height: unset;
      color: #fff;
      padding: 0.8rem 0.85rem;
      margin-top: 1rem;
    }

    svg {
      width: 24px;
      vertical-align: middle;
      fill: white;
    }
  }

  @media (min-width: 60rem) {
    .text__input {
      display: none;
    }
  }

  @media (max-width: 60rem) {
    width: 100%;
    flex-direction: column;
    border: none;
    box-shadow: none;
    background: transparent;
    padding: 0;

    svg {
      display: none;
    }
  }
}
</style>
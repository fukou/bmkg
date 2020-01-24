<template>
  <nav>
    <ul>
      <li>
        <nuxt-link to="/" exact>Beranda</nuxt-link>
      </li>
      <li>
        <nuxt-link to="/tentang" exact>Tentang</nuxt-link>
      </li>
      <li>
        <a href="http://www.bmkg.go.id/" rel="noopener noreferrer" target="_blank">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <g fill="none" fill-rule="evenodd">
              <path
                d="M18 14v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8c0-1.1.9-2 2-2h5M15 3h6v6M10 14L20.2 3.8"
              />
            </g>
          </svg> Website utama
        </a>
      </li>
    </ul>
  </nav>
</template>

<style lang="scss">
nav {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: auto;
  border-bottom: 1px solid #ddd;
  padding: 0 5rem;
  z-index: 999;
  background: rgba(#fff, 0.85);
  // backdrop-filter: blur(8px);

  @media (max-width: 60rem) {
    display: none;
  }

  ul {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: flex-start;
    list-style: none;
    margin-left: 0;
    padding: 0;

    @media (max-width: 60rem) {
      justify-content: center;
    }

    li {
      margin: 0;
      a {
        display: block;
        padding: 1.35rem 1.85rem;
        cursor: pointer;
        color: #111;
        text-decoration: none;
        margin: 0;

        @media (max-width: 40rem) {
          padding: 1.1rem 1.25rem;

          svg {
            display: none;
          }
        }

        svg {
          vertical-align: middle;
          margin-right: 0.5rem;
        }

        @media (max-width: 60rem) {
          font-size: 0.85em;
        }
      }

      .nuxt-link-active {
        font-weight: 600;
        border-bottom: 4px solid #8487c2;
      }
    }
  }
}
</style>
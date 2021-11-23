<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <div class="cursor" @click="MoveTo">
          <img src="logo.png" alt="LOGO" width="150" height="30" class="logoTag">
        </div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <span v-if="this.$store.state.isLogin">
              <router-link class="nav-link active d-flex" :to="{ name: 'RecommendUser' }">RecommendUser</router-link>
              <!-- <router-link class="nav-link active" :to="{ name: 'MovieList' }">MovieList</router-link> -->
            </span>
          </div>
        </div>
      </div>
    </nav>
    <router-view @login="this.$store.state.isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    MoveTo: function () { // 그 페이지에서 누르면 에러
      if (this.$store.state.isLogin) {
        this.$router.push({
          name: 'MovieList'
        })
      } else {
        this.$router.push({
          name: 'Main'
        })
      }
    }
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  
}

.nav {
  text-align: center;
  padding: 10px;
  position: relative;
  z-index: 99;
  background-color: black;
}

#nav a {
  font-weight: bold;
  color: #6f42c1;
  
}

#nav a.router-link-exact-active {
  color: #d63384;
  

}

#logo {
  color: #f8067f;
  font-weight: bold;
  
  text-align: left;
  padding: 10px;
}

.logoTag {
  position: relative;
  z-index: 99;
}

.cursor {
  cursor: pointer;
}
</style>

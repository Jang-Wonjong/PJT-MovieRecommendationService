<template>
  <div id="app">
    <h1 id='logo'>Movie&Chill</h1>
    <div id="nav" class="navbar navbar-expand-lg navbar-dark bg-dark">
      <router-link :to="{ name: 'Main' }">Main</router-link> |
      <span v-if="this.$store.state.isLogin">
        <router-link :to="{ name: 'RecommendUser' }">RecommendUser</router-link> |
        <router-link :to="{ name: 'MovieList' }">MovieList</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> |
      </span>
    </div>
    <router-view @login="this.$store.state.isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  
}

#nav {
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
</style>

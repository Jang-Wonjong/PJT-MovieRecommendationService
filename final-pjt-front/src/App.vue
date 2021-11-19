<template>
  <div id="app">
    <h1 id='logo'>Movie&Chill</h1>
    <div id="nav" class="navbar navbar-expand-lg navbar-dark bg-dark">
      <span v-if="isLogin">
        <router-link :to="{ name: 'MovieList' }">MovieList</router-link> |
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> |
      </span>
    </div>
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
    
  },
  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.isLogin = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: black;
}

#nav {
  padding: 10px;
  background-color: black;
}

#nav a {
  font-weight: bold;
  color: #6f42c1;
  background-color: black;
}

#nav a.router-link-exact-active {
  color: #d63384;
  background-color: black;

}

#logo {
  color: #f8067f;
  font-weight: bold;
  background-color: black;
  text-align: left;
  padding: 10px;
}
</style>

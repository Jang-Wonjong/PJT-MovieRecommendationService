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
        <div class="collapse navbar-collapse w-100" id="navbarNavAltMarkup">
          <div class="navbar-nav" v-if="this.$store.state.isLogin">
            <router-link class="nav-link active mx-2" :to="{ name: 'RecommendUser' }">RecommendUser</router-link>
          </div>
          <div class="navbar-nav" v-if="this.$store.state.isLogin" @click="moveToProfile(meId)">
            <img src="https://occ-0-395-325.1.nflxso.net/dnm/api/v6/K6hjPJd6cR6FpVELC5Pd6ovHRSk/AAAABTzQndLIMejbjN7Yj6nzQHf0AffS5Whagu7Q4pYGeKpPxuO2brcmZvB729F3MQpEw6V4T1_vDzftgFBGpHFh18J9BEng.png?r=f79" alt=""
              width="50"
              class="p-2 cursor profile"
            >
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
  data: function () {
    return {
      meId: this.$store.state.id
    }
  },
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
    },
    moveToProfile: function (userId) {
      // console.log(userId)
      this.$router.push({
        name: 'UserProfile',
        query: { userId }  
      })
    }
  }
}
</script>

<style scoped>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
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

/* .profile {
  
} */
</style>

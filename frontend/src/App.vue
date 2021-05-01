<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/login">About</router-link>
      <button v-if="hasAuth" class="btn btn-info" @click="logout">Logout</button>
    </div>
    <router-view/>
  </div>
</template>
<script>
    import {request} from "./request";
    import {appConfig} from "./appConfig";

    export default {
        name: 'App',
        created: async function () {
            const token = localStorage.getItem('token')
            if (token) {
                request.defaults.headers['Authorization'] = `Token ${token}`
                try {
                    const res = await request.get(appConfig.CURRENT_USER_PATH)
                    const {data} = res
                    await this.$store.dispatch("setCurrentUser", data)
                    await this.$store.dispatch("setHasAuth", true)
                } catch (e) {
                    localStorage.setItem('token', '')
                    this.$router.push('/login')
                    console.log("Error : ", e)
                }
            }
        },
        computed: {
            hasAuth () {
                return this.$store.state.hasAuth
            }
        },
        methods: {
            async logout() {
                try {
                    const res = await request.get(appConfig.LOGOUT_PATH)
                    if (res.status === 200) {
                        localStorage.setItem('token', '')
                        request.defaults.headers['Authorization'] = ''
                        this.$store.dispatch('clearCurrentUser')
                        this.$router.push('/login')
                    }
                } catch (e) {
                    console.log("Error : ", e)
                }
            }
        }
    }
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
  
  #nav {
    padding: 30px;
  }
  
  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  
  #nav a.router-link-exact-active {
    color: #42b983;
  }
</style>

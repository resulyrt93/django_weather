<template>
  <div class="about">
    <div class="login-container">
      <div class="login-card">
        <b-alert v-if="loginError" show>Default Alert</b-alert>
        <form @submit="login">
          <p class="h4 text-center mb-4">Login</p>
          <label for="username-field" class="grey-text">Username</label>
          <input v-model="username" type="text" id="username-field" class="form-control"/>
          <br/>
          <label for="password-field" class="grey-text">Password</label>
          <input type="password" v-model="password" id="password-field" class="form-control"/>
          <div class="text-center mt-4">
            <button class="btn btn-unique" type="submit">Login</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
    import {request} from "../request";
    import {appConfig} from "../appConfig";

    export default {
        name: 'Login',
        data: () => {
            return {
                username: '',
                password: '',
                loginError: false
            }
        },
        methods: {
            async login(e) {
                e.preventDefault()
                this.loginError = false
                const {username, password} = this
                try {
                    const res = await request.post(appConfig.TOKEN_AUTH_PATH, {username, password})
                    const {data: {token}} = res
                    localStorage.setItem('token', token);
                    request.defaults.headers['Authorization'] = `Token ${token}`
                    this.$store.dispatch("setHasAuth", true)
                    this.$router.push('/')
                } catch (e) {
                    console.log("error : ", e)
                    this.loginError = true
                }
            }
        }
    }
</script>

<style>
  .login-container {
    display: flex;
    justify-content: center;
  }
  .login-card {
    width: 400px;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
  }
</style>

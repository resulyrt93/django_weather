<template>
  <div class="d-flex justify-content-center mt-5">
    <div class="register-card mx-4 p-3">
      <form @submit="register">
        <p class="h4 text-center mb-4">Register</p>
        <label for="username-field" class="grey-text">Username</label>
        <input v-model="username" type="text" id="username-field" class="form-control"/>
        <br/>
        <label for="password-field" class="grey-text">Password</label>
        <input type="password" v-model="password" id="password-field" class="form-control"/>
        <br/>
        <label for="email-field" class="grey-text">Email</label>
        <input type="email" v-model="email" id="email-field" class="form-control"/>
        <div class="text-center mt-4">
          <button class="btn btn-unique" type="submit">Register</button>
        </div>
      </form>
      <b-alert class="mt-2" variant="warning" v-if="loginError" show>{{errorText}}</b-alert>
    </div>
  </div>
</template>

<script>
    import {request} from "../request";
    import {appConfig} from "../appConfig";

    export default {
        name: "Register",
        data: () => {
            return {
                username: '',
                password: '',
                email: '',
                loginError: false,
                errorText: '',
            }
        },
        methods: {
            async register(e) {
                this.loginError = false
                this.errorText = ''
                e.preventDefault()
                const {username, password, email} = this
                try {
                    const res = await request.post(appConfig.REGISTER_PATH, {username, password, email})
                    const {data: {token}} = res
                    localStorage.setItem('token', token);
                    request.defaults.headers['Authorization'] = `Token ${token}`
                    await this.$store.dispatch("setHasAuth", true)
                    this.$router.push('/')
                } catch (e) {
                    console.log("error : ", e.response.data)
                    const {detail} = e.response.data
                    this.errorText = detail
                    this.loginError = true
                }
            }
        }
    }
</script>

<style scoped>
  .register-card {
    width: 400px;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
  }
</style>

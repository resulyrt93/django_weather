import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {
            forNotAuth: true
        }
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
        meta: {
            forNotAuth: true
        }
    }
]

const router = new VueRouter({
    routes
})

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token')
    if (to.matched.some(record => record.meta.requiresAuth) && !token) {
        next({
            path: '/login',
            params: {nextUrl: to.fullPath}
        })
    } else if (to.matched.some(record => record.meta.forNotAuth) && token) {
        next('/')
    } else {
        next()
    }
})

export default router

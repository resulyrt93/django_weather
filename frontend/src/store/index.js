import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currentUser: {},
        hasAuth: false
    },
    mutations: {
        setCurrentUser(state, data) {
            state.currentUser = data
        },
        setHasAuth(state, value) {
            state.hasAuth = value
        }
    },
    actions: {
        setCurrentUser(context, data) {
            context.commit('setCurrentUser', data)
        },
        clearCurrentUser(context) {
            context.commit('setCurrentUser', {})
            context.commit('setHasAuth', false)
        },
        setHasAuth(context, value) {
            context.commit('setHasAuth', value)
        }
    },
    modules: {}
})

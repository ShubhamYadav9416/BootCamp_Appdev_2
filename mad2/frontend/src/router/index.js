import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from "../views/Home.vue"
import RegisterView from "../views/RegisterView.vue"
import LoginView from '@/views/LoginView.vue';

Vue.use(VueRouter)

const routes =[
    {
        path: "/",
        name:"User-Home",
        component: Home
    },
    {
        path: "/register",
        name:"Register-Page",
        component: RegisterView
    },
    {
        path: "/login",
        name:"Login-Page",
        component: LoginView
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router;


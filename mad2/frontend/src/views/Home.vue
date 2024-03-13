<template>
    <div>
        "hey! I am in Home.vue"
        <router-link to="/register">Register</router-link><br>
        <router-link to="/login">Login</router-link>
        <button @click="logoutUser()">LogOut</button>

</div>
</template>

<script>
export default{
    name:'UserHome',
    methods:{
        logoutUser(){
            localStorage.removeItem("access_token")
            localStorage.removeItem("refresh_token")
            localStorage.removeItem("user_mail")

            alert("user log out!!!!")
            this.$router.push("/login")
        }
    }
}
</script>

<style scoped>
</style>
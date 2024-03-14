<template>
    <div>
        <Header></Header>
        "hey! I am in Home.vue"
        <router-link to="/register">Register</router-link><br>
        <router-link to="/login">Login</router-link>
        <button @click="logoutUser()">LogOut</button>
    <div v-for="user in all_users_data" :key="user.user_id" v-show="all_users_data">
        {{ user.user_mail }}
    </div>
    <div v-if="x == true">
        {{all_users_data}}
    </div>
    <FlashMessage :position="'right bottom'"></FlashMessage>


</div>
</template>

<script>
import axios from 'axios'
import Header from '@/components/Header.vue'

export default{
    name:'UserHome',
    components: {
        Header
    },
    data(){
        return{
            all_users_data : {},
            x: false
        }
    },
    methods:{
        logoutUser(){
            localStorage.removeItem("access_token")
            localStorage.removeItem("refresh_token")
            localStorage.removeItem("user_mail")

            alert("user log out!!!!")
            this.$router.push("/login")
        },
        async getAllUserData(){
            try{
                let access_token = localStorage.getItem('access_token')

                axios.defaults.headers.common['Authorization'] ='Bearer ' + access_token
                const dataResponse =  await axios.get(`http://127.0.0.1:8081/api/user`)

                console.log(dataResponse)

                this.all_users_data = dataResponse.data
                this.x = false

                this.flashMessage.success({
                    message: "user data retrieved"
                });
                this.flashMessage.error({
                    message: "user data retrieved"
                });
                this.flashMessage.warning({
                    message: "user data retrieved"
                });
                this.flashMessage.info({
                    message: "user data retrieved"
                });


            }
            catch(error){
                console.log(error)
                alert("error while fetching data")
            }
        }
    },
    created(){
        this.getAllUserData()
    }

}
</script>

<style scoped>
</style>
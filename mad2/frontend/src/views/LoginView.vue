<template>
<div>

    <b-container class="bv-example-row">
            <b-row>
                <b-col>1 of 3</b-col>
                <b-col>
                    <h1>login Page</h1>
                    <b-form>
                        <b-form-group id="input-group-1" label="Email address:" label-for="input-1"
                            >
                            <b-form-input id="input-1" v-model="form.email" type="text" placeholder="Enter email"
                                required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
                            <b-form-input id="input-2" v-model="form.password" placeholder="Enter Password"
                                required></b-form-input>
                        </b-form-group>
                        
       
                        <b-button type="button" variant="primary" @click="loginUser()">Submit</b-button>
                        <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>
                    </b-form>
                    <b-card class="mt-3" header="Form Data Result">
                        <pre class="m-0">{{ form }}</pre>
                    </b-card></b-col>
                <b-col>3 of 3</b-col>
            </b-row>
        </b-container>
</div>

</template>

<script>

import axios from 'axios';

export default {

    name: 'LoginUserView',
    data() {
        return {
            form: {
                email: "",
                password: "",

            }

        }
    },
    methods:{
    resetForm() {
            this.form.email = "";
            this.form.password = ""
        },
        loginUser() {


            if(!this.form.email || !this.form.password){
                alert("All fields are required")
                return;
            }

            if(!this.form.email.includes("@") || !this.form.email.endsWith(".com")){
                alert("invalid email");
                return;
            }


            axios.post("http://127.0.0.1:8081/api/user/login",{
                user_mail : this.form.email,
                password: this.form.password,
            })
            .then((response) => {
                if (response.data.status == "success"){
                    // alert(response.data.message)
                    // console.log(response.data)
                    // this.$router.push('/login')
                    const access_token = response.data.access_token;
                    const refresh_token = response.data.refresh_token;
                    const user_mail = response.data.user_mail

                    localStorage.setItem("access_token", access_token)
                    localStorage.setItem("refresh_token", refresh_token)
                    localStorage.setItem("user_mail",user_mail)


                    // console.log(response.data)
                    this.$router.push("/")
                    return;
                }
                if (response.data.status == "failed"){
                    alert(response.data.message)
                }

            })
            .catch((error) => {
                console.error(error);
                alert("An error occurred  while registering")
            })

        }

}}
</script>


<style scoped></style>
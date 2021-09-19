<template>
    <div>
        <div class="columns mt-6">
            <div class="column is-4 is-offset-4 box">

                <div class="content">
                    <h1 class="has-text-centered">
                        Sign Up
                    </h1>
                </div>

                <div class="field">
                    <label  class="lable">Username</label>
                    <div class="control">
                        <input type="text" class="input">
                    </div>
                    <p class="help">Write your username</p>
                </div>

                <div class="field">
                    <label  class="lable">Email</label>
                    <div class="control">
                        <input type="email" class="input">
                    </div>
                    <p class="help">Write your email</p>
                </div>

                <div class="field">
                    <label  class="lable">Password</label>
                    <div class="control">
                        <input type="password" class="input">
                    </div>
                    <p class="help">Write your password</p>
                </div>

                <div class="field">
                    <label  class="lable">Password</label>
                    <div class="control">
                        <input type="password" class="input">
                    </div>
                    <p class="help">Repeat your password</p>
                </div>

                <div class="has-text-centered">
                    <button class="button is-info is-medium">Registration</button>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name : "SignUp",

    data(){
        return {
            username : "",
            email : "",
            password : "",
            password2: "",
        }
    },

    methods : {
        
    }
}
</script>
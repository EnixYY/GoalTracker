<template>
    <form @submit.prevent="submitSignUpDetails">
        <div>
        <label>Name</label>
        <input type="text" v-model="name">
        </div>
        <div>
        <label>Email</label>
        <input type="email" v-model="email">
        </div>
        <div>
        <label>Role</label>
        <input type="text" v-model="role">
        </div>
        <div>
        <label>Department</label>
        <input type="text" v-model="department">
        </div>
        <div>
        <label>Password</label>
        <input type="password" v-model="password">
        </div>
        <button>Sign up</button>
    </form>
</template>

<script>
export default {
    name:"SignUpForm",
    emits:["sign-up"],
    data(){
        return{
            name:"",
            email:"",
            role:"",
            department:"",
            password:"",
        }
    },
    methods:{
    submitSignUpDetails(){
        this.$emit(
            "sign-up", 
            this.name, 
            this.email, 
            this.role, 
            this.department, 
            this.password, 
        )
    }
    }
}
</script>

<style>

</style>

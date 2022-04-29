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
        <input type="text" v-model="password">
        </div>
        <div>
        <label>Confirm Password</label>
        <input type="text" v-model="confirmPassword">
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
            confirmPassword:"",
        }
    },
    methods:{
    submitSignUpDetails(){
        this.$emit(
            'sign-up', 
            this.name, 
            this.email, 
            this.role, 
            this.department, 
            this.password, 
            this.confirmPassword,
        )
    }
    }
}
</script>

<style>

</style>

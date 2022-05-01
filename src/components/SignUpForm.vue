<template>
    <form id="signupForm" @submit.prevent="submitSignUpDetails">
        <div class="individual">
        <label>Name</label>
        <input type="text" v-model="name">
        </div>
        <div class="individual">
        <label>Email</label>
        <input type="email" v-model="email">
        </div>
        <div class="individual">
        <label>Role</label>
        <input type="text" v-model="role">
        </div>
        <div class="individual">
        <label>Department</label>
        <input type="text" v-model="department">
        </div>
        <div class="individual">
        <label>Password</label>
        <input type="password" v-model="password">
        </div>
        <div class="individual">
        <button>Sign up</button>
        </div>
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

<style scoped>
#signupForm{
    display: flex;
    flex-direction: column;
    width: 100vw;
}
.individual{
    display:flex;
    justify-content: center;
    padding: 10px;
}
button{
    width: 80px;
    padding: 6px;
    text-align: center;
    border-radius: 10px;
    background-color: turquoise;
    border: 1px solid black;
    color: white;
}
button:hover{
    color: black;
}
label{
    font-weight: bold;
    padding-right: 10px;
}
</style>

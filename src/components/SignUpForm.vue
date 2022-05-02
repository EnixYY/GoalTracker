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
        <select v-model="role">
            <option value="Manager">Manager</option>
            <option value="Employee">Employee</option>
        </select>
        </div>
        <div class="individual">
        <label>Department</label>
        <select v-model="department">
            <option value="IT">IT</option>
            <option value="Sales">Sales</option>
            <option value="HR">HR</option>
            <option value="Marketing">Marketing</option>
        </select>
        </div>
        <div class="individual">
            <label>Password</label>
            <input type="password" v-model="password">
        </div>
        <div class="individual">
            <label v-if="errorChecker">Please create again as there is an error while creating</label>
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
    props:['errorChecker'],
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
    background-color: turquoise;
    width: 70vw;
    height: 40vh;
    justify-content: center;
    border-radius: 10px;
    margin-left: 115px;
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
    background-color: white;
    border: 1px solid black;
    color: black;
}
button:hover{
    color: white;
    background-color: turquoise;
}
label{
    font-weight: bold;
    padding-right: 10px;
}
</style>

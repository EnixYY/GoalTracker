<template>
<div id="assignedPageHolder">
    <div>
        <SideNavBar :is-manager="isManager" :user-name="userName"/>
    </div>
    <div id="goalsHolder">
        <GoalsCard 
        v-for="goal in this.departmentGoalsData[0]" 
        :key="goal.id" 
        :goal-title="goal.name"
        :due-date="goal.endDate"
        :full-value="goal.value"
        :user-input="goal.totalUserContribution"
        :is-manager="isManager" 
        />
    </div>
</div>
</template>;

<script>
import GoalsCard from "../components/GoalsCard.vue"
import SideNavBar from "../components/SideNavBar.vue"
import jwt_decode from "jwt-decode";
import axios from "axios"
import router from "../router"


export default {
    name: "ManagerViewAllDepartmentGoals",
    components: {
        GoalsCard,
        SideNavBar,
    },
    data(){
        return{
        userId:"",
        isManager:"",
        userData:[],
        userName:"",
        userDepartment:"",
        departmentGoalsData:[],
    }
    },
    created(){
        this.decodeToken()
        this.getUser()
    },
    methods:{
        decodeToken(){
            const that = this;
            const token = localStorage.accessToken
            const decode = jwt_decode(token)
            that.userId = decode.user_id
        },
        getUser(){
            const that = this;
            const config = {
            method: 'get',
            url: `http://127.0.0.1:8000/account/get-account/${that.userId}`,
            headers: { }
            };

            axios(config)
            .then(function (response) {
            that.userData.push(response.data)
            console.log(that.userData);
            console.log(response.data);
            that.checkUser()
            that.userName = response.data.name
            that.userDepartment = response.data.department
            that.getDeparment()
            if (response.data.role === "Manager"){
            that.isManager = true
            }else{
                that.isManager = false
            }
            })
            .catch(function (error) {
            console.log(error);
            });
        },
        checkUser(){
        if(this.userData[0].email !== localStorage.email && !localStorage.accessToken){
            router.push({name: 'home'})
        }
    },
        getDeparment(){
            const that = this;
            const config = {
            method: 'get',
            url: `http://127.0.0.1:8000/api/get-department-goals/${that.userDepartment}/`,
            headers: { }
            };

            axios(config)
            .then(function (response) {
            const timeNow = new Date().getTime()
            const DepartmentGoalsData = response.data
            const filteredData = DepartmentGoalsData.filter((goal)=> { 
            return new Date(goal.endDate).getTime() >= timeNow})
            that.departmentGoalsData.push(filteredData)
            console.log(that.departmentGoalsData[0]);
            })
            .catch(function (error) {
            console.log(error);
            });
        },
    }
}
</script>

<style scoped>
#assignedPageHolder {
    display: flex;
    background-color: white;
}
#goalsHolder{
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    height: 100vh;
    width: 75vw;
    padding-left: 25vw
}
</style>
<template>
<div id="assignedPageHolder">
    <div>
        <SideNavBar :is-manager="isManager" :user-name="userName"/>
    </div>
    <div id="goalsHolder">
        <GoalsCard 
        v-for="goal in employeeProgressData[0]" 
        :key="goal.id" 
        :goal-title="goal.departmentGoalName"
        :due-date="goal.endDate"
        :full-value="goal.individualValue"
        :user-input="goal.employeeInput"
        :department-goal-id="goal.departmentGoalsId"
        :user-id-for-progress="goal.userId"
        :is-manager="isManager"
        />
    </div>
</div>
</template>;

<script>
import GoalsCard from "../components/GoalsCard.vue"
import SideNavBar from "../components/SideNavBar.vue"
import axios from "axios"
import router from "../router"
import jwt_decode from "jwt-decode";

export default {
    name: "AssignedGoals",
    components: {
        GoalsCard,
        SideNavBar,
    },
    data(){
        return{
        isManager: false,
        userData: [],
        departmentGoalsData: [],
        userName: "",
        userId: "",
        employeeProgressData: [],
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
        checkUser(){
            if(this.userData[0].email !== localStorage.email && !localStorage.accessToken){
                router.push({name: 'home'})
            }
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
            that.checkUser()
            that.userName = response.data.name
            that.getEmployeeProgress()
            })
            .catch(function (error) {
            console.log(error);
            });
        },
        getEmployeeProgress(){
            const that = this;
            const config = {
                method: 'get',
                url: `http://127.0.0.1:8000/api/get-progress-by-userid/${that.userId}/`,
                headers: { }
                };

                axios(config)
                .then(function (response) {
                that.employeeProgressData.push(response.data)
                console.log(that.employeeProgressData[0]);
                })
                .catch(function (error) {
                console.log(error);
                });
        }
    }, 
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
}
</style>
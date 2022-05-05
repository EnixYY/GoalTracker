<template>
<div id="CreateGoalsPageHolder">
    <div>
        <SideNavBar :is-manager="isManager" :user-name="userName"/>
        </div>
    <div id="mainHolder">
            <CreateGoalForm @create-goal="createGoal" :user-details="userDetailsForEmployeeInDepartment[0]"/>
    <div v-if="error" id="error">
        <label>{{errorMessage}}</label>
    </div>  
    </div>
</div>
</template>

<script>
import CreateGoalForm from '../components/CreateGoalForm.vue'
import SideNavBar from '../components/SideNavBar.vue'
import router from '../router'
import jwt_decode from "jwt-decode";
import axios from "axios"

export default {
    name: "CreateGoals",
    components: {
    CreateGoalForm,
    SideNavBar,
},
data(){
    return{
        userData:[],
        userId:"",
        isManager:"",
        userName:"",
        userDepartment:"",
        numberOfEmployeeInDepartment:"",
        userDetailsForEmployeeInDepartment:[],
        departmentGoalNameForProgressUpdate:"",
        error: false,
        errorMessage: "",
    }
},
created(){
    this.decodeToken()
    this.getUser()
},
methods:{
    checkUser(){
        if(this.userData[0].email !== localStorage.email && !localStorage.accessToken){
            router.push({name: 'home'})
        }
        },
    createGoal(goal, endDate, value, allocation, percentage, isAssigned){
        if(goal === ""){
            this.error = true
            this.errorMessage = "Please fill in the Goal."
        }else if(endDate === ""){
            this.error = true
            this.errorMessage = "Please select a End Date."
        }else if(value === ""){
            this.error = true
            this.errorMessage = "Please fill in the Value."
        }else if(allocation === ""){
            this.error = true
            this.errorMessage = "Please select the Allocation Type."
        }else{
        const that = this;
        const data = JSON.stringify({
            "name": goal,
            "value": value,
            "department": this.userDepartment,
            "endDate": endDate,
            "number_of_employee": this.numberOfEmployeeInDepartment,
            "allocation_type": allocation,
            "totalUserContribution": 0,
            });
            that.departmentGoalNameForProgressUpdate = goal
            
            const config = {
            method: 'put',
            url: 'http://127.0.0.1:8000/api/create-department-goals/',
            headers: { 
                'Content-Type': 'application/json'
            },
            data : data
            };
            axios(config)
            .then(function (response) {
            if(isAssigned === false){
            that.userDetailsForEmployeeInDepartment[0].map((data, i)=>{
                const individualAmount = response.data.value/that.numberOfEmployeeInDepartment
                const progressData = JSON.stringify({
                    "individualValue": Math.ceil(individualAmount),
                    "departmentGoalsId": response.data.id,
                    "userId": that.userDetailsForEmployeeInDepartment[0][i].id,
                    "departmentGoalName": that.departmentGoalNameForProgressUpdate,
                    "endDate": endDate,
                    });
                    const config = {
                    method: 'put',
                    url: 'http://127.0.0.1:8000/api/create-progress/',
                    headers: { 
                        'Content-Type': 'application/json'
                    },
                    data : progressData
                    };

                    axios(config)
                    .then(function (response) {
                    router.push({name: 'home'})
                    return response.data
                    })
                    .catch(function (error) {
                    console.log(error);
                    });
            })
            }else if(isAssigned === true){
                that.userDetailsForEmployeeInDepartment[0].map((data, i)=>{
                    const individualAmount = percentage[i]*response.data.value/100
                    const progressData = JSON.stringify({
                        "individualValue": Math.ceil(individualAmount),
                        "departmentGoalsId": response.data.id,
                        "userId": that.userDetailsForEmployeeInDepartment[0][i].id,
                        "departmentGoalName": that.departmentGoalNameForProgressUpdate,
                        "endDate": endDate,
                        });
                        const config = {
                        method: 'put',
                        url: 'http://127.0.0.1:8000/api/create-progress/',
                        headers: { 
                            'Content-Type': 'application/json'
                        },
                        data : progressData
                        };

                        axios(config)
                        .then(function (response) {
                        router.push({name: 'home'})
                        return response.data
                        })
                        .catch(function (error) {
                        console.log(error);
                        });
            })
            }
            })
            .catch(function (error) {
            console.log(error);
            });
        }
    },
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
            that.checkUser()
            that.userName = response.data.name
            that.userDepartment = response.data.department
            that.getNumberOfUserInDepartment()
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
        getNumberOfUserInDepartment(){
            const that = this;
            const config = {
                method: 'get',
                url: `http://127.0.0.1:8000/account/get-department/${that.userDepartment}/`,
                headers: { }
                };
                axios(config)
                .then(function (response) {
                that.numberOfEmployeeInDepartment = response.data.length;
                that.userDetailsForEmployeeInDepartment.push(response.data)
                })
                .catch(function (error) {
                console.log(error);
                });
        }
}
}
</script>

<style scoped>
#CreateGoalsPageHolder {
    display: flex;
    background-color: white;
}
#mainHolder{
    padding-left: 25vw
}
#error{
    display: flex;
    flex-direction: column;
    width: 100vw;
    background-color: salmon;
    width: 66vw;
    height: 10vh;
    justify-content: center;
    border-radius: 10px;
    margin-left: 35px;
}
</style>
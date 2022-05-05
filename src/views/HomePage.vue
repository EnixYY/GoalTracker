<template>
    <div id="HomePageHolder">
        <div>
        <SideNavBar :is-manager="isManager" :user-name="userName"/>
        </div>
        <div id="contentHolder">
        <WelcomeCard :user-name="userName"/>
        <OverallGoalsCard 
        :is-manager="isManager" 
        :user-name="userName" 
        :department="userDepartment"
        :department-goals-data="departmentGoalsData[0]"
        :user-progress-data="employeeProgressData[0]"
        />
        </div>
    </div>
</template>;

<script>
import WelcomeCard from "../components/WelcomeCard.vue"
import OverallGoalsCard from "../components/OverallGoalsCard.vue"
import SideNavBar from "../components/SideNavBar.vue"
import axios from "axios"
import router from "../router"
import jwt_decode from "jwt-decode";


export default {
    name:"HomePage",
    components:{
        WelcomeCard,
        OverallGoalsCard,
        SideNavBar,
    },
    data(){
        return{
            userData: [],
            departmentGoalsData: [],
            isManager: null,
            userName: "",
            userDepartment: "",
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
            const DepartmentGoalsDataRaw = response.data
            const filteredData = DepartmentGoalsDataRaw.filter((goal)=> { 
            return new Date(goal.endDate).getTime() >= timeNow})
            that.departmentGoalsData.push(filteredData)
            console.log(that.departmentGoalsData[0]);
            that.getDepartmentContributedValue()
            })
            .catch(function (error) {
            console.log(error);
            });
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
            console.log(that.userData)
            console.log(response.data);
            that.checkUser()
            that.userName = response.data.name
            that.userDepartment = response.data.department
            that.getDeparment()
            if (response.data.role === "Manager"){
            that.isManager = true
            }else{
                that.isManager = false
                that.getEmployeeProgress()
            }
            })
            .catch(function (error) {
            console.log(error);
            });
        },
        getDepartmentContributedValue(){
            this.departmentGoalsData[0].map((data, i)=>{
                const that = this;
                console.log(that.departmentGoalsData[0][i].id)
                const config = {
                method: 'get',
                url: `http://127.0.0.1:8000/api/get-progress/${that.departmentGoalsData[0][i].id}/`,
                headers: { }
                };

                axios(config)
                .then(function (response) {
                    console.log(that.departmentGoalsData[0][i].id, response.data)
                if(response.data.length !== 0){
                    console.log(response.data)
                        const totalValueOfUser = response.data.reduce((previous, current)=>{
                                                console.log(typeof previous, typeof current.employeeInput)
                            return parseInt(previous) + parseInt(current.employeeInput)
                        }, 0)
                                        console.log(that.departmentGoalsData[0][i].id, response.data)
                const data = JSON.stringify({
                    "totalUserContribution": totalValueOfUser  
                });
                console.log(that.departmentGoalsData[0][i].id, totalValueOfUser)
                const config = {
                method: 'patch',
                url: `http://127.0.0.1:8000/api/update-user-input/${that.departmentGoalsData[0][i].id}/`,
                headers: { 
                    'Content-Type': 'application/json'
                },
                data : data
                };

                axios(config)
                .then(function (response) {
                console.log(response.data);
                })
                .catch(function (error) {
                console.log(error);
                });               
                }else{
                const data = JSON.stringify({
                    "totalUserContribution": 0  
                });

                const config = {
                method: 'patch',
                url: `http://127.0.0.1:8000/api/update-user-input/${that.departmentGoalsData[0][i].id}/`,
                headers: { 
                    'Content-Type': 'application/json'
                },
                data : data
                };

                axios(config)
                .then(function (response) {
                console.log(response.data);
                })
                .catch(function (error) {
                console.log(error);
                });                        }
                }
                )
                .catch(function (error) {
                console.log(error);
                });
            })
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
                const timeNow = new Date().getTime()
                const progressData = response.data
                const filteredData = progressData.filter((progress)=> { 
                return new Date(progress.endDate).getTime() >= timeNow})
                that.employeeProgressData.push(filteredData)
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
#HomePageHolder {
    display: flex;
    background-color: white;
}
#contentHolder{
    display: flex;
    flex-direction: column;
    padding: 18px;
    padding-left: 27vw
}
</style>
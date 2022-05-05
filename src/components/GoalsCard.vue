<template>
    <div class="goalcard">
        <h4>{{goalTitle}}</h4>
        <h4>{{userInputLabel}}/{{fullValue}}</h4>
        <h4>Due on {{dueDate}}</h4>
        <button @click="setIdEdit" v-if="isManager === false && isEdit === false">Edit</button>
        <form v-if="isManager === false && isEdit" @submit.prevent="updateUserNewInput">
        <input v-model="userNewInput"/>
        <button>Add Progress</button>
        </form>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name:"GoalsCard",
    data(){
        return{
            isEdit: false,
            userInputLabel: this.userInput,
            userNewInput: "",
        }
    },
    props:[
        'goalTitle',
        'fullValue',
        'dueDate',
        'userInput',
        'isManager',
        'departmentGoalId',
        'userIdForProgress',
    ],
    methods:{
        setIdEdit(){
            this.isEdit = true
        },
        updateUserNewInput(){
            const that = this;
            const updatedUserinput = parseInt(that.userNewInput) + parseInt(this.userInputLabel)
            const data = JSON.stringify({
                "employeeInput": updatedUserinput
                });

                var config = {
                method: 'patch',
                url: `http://127.0.0.1:8000/api/update-progress/${that.departmentGoalId}/${that.userIdForProgress}/`,
                headers: { 
                    'Content-Type': 'application/json'
                },
                data : data
                };

                axios(config)
                .then(function (response) {
                that.userInputLabel = updatedUserinput
                that.isEdit = false
                that.userNewInput = ""
                return response.data
                })
                .catch(function (error) {
                console.log(error);
                });
        }
    }
}
</script>

<style>
.goalcard {
        background-color: turquoise;
        justify-content: center;
        border: 1px solid black;
        border-radius: 10px;
        padding: 10px;
        width: 200px;
        height: 33vh;
        margin-top: 80px
}
button{
    margin-top: 10px;
    width: 100px;
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
</style>
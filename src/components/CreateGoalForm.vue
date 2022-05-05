<template>
    <form id="createGoalsForm" @submit.prevent="submitGoalsDetails">
        <div class="individual">
        <label>Goal</label>
        <input type="text" v-model="goal">
        </div>
        <div class="individual">
        <label>End Date</label>
        <input type="date" v-model="endDate">
        </div>
        <div class="individual">
        <label>Value</label>
        <input type="number" v-model="value">
        </div>
        <div class="individual">
        <label>Allocation</label>
        <select v-model="allocation">
            <option value="Equally">Equally</option>
            <option value="Assigned">Assigned</option>
        </select>
        </div>
        <div class="individual">
        <label v-if="isAssigned">Name of Employee</label>
        <input v-if="isAssigned" type="text" v-model="nameOfEmployee">
        </div>
        <div class="individual">
        <label v-if="isAssigned">Percentage</label>
        <input v-if="isAssigned" type="number" v-model="percentage">
        </div>
        <div class="individual">
        <button v-if="isAssigned">Add more Employee</button>
        </div>
        <div class="individual">
        <button>Create Goal</button>
        </div>
    </form>
</template>

<script>
export default {
    name:"CreateGoalForm",
    emits:["create-goal"],
    data(){
        return{
            isAssigned:false,
            goal:"",
            endDate:"",
            value:"",
            allocation:"",
            nameOfEmployee:"",
            percentage:"",
        }
    },
    methods:{
    submitGoalsDetails(){
        this.$emit(
            "create-goal", 
            this.goal, 
            this.endDate, 
            this.value, 
            this.allocation, 
            this.nameOfEmployee, 
            this.percentage,
        )
    }
    }
}
</script>

<style scoped>
#createGoalsForm{
    display: flex;
    flex-direction: column;
    width: 500px;
    height: 400px;
    background-color: turquoise;
    border-radius: 10px;
    justify-content: center;
    margin-top: 200px;
    margin-left: 35px;
}
.individual{
    display:flex;
    justify-content: center;
    padding: 10px;
}
button{
    width: 120px;
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
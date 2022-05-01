<template>
    <div id="HomePageHolder">
        <div>
        <SideNavbar/>
        </div>
        <div id="contentHolder">
        <WelcomeCard/>
        <OverallGoalsCard/>
        </div>
    </div>
</template>;

<script>
import WelcomeCard from "../components/WelcomeCard.vue"
import OverallGoalsCard from "../components/OverallGoalsCard.vue"
import SideNavbar from "../components/SideNavBar.vue"

export default {
    name:"HomePage",
    components:{
        WelcomeCard,
        OverallGoalsCard,
        SideNavbar,
    }
}
</script>

<style>
#HomePageHolder {
    display: flex;
    background-color: white;
}
#contentHolder{
    display: flex;
    flex-direction: column;
    padding: 18px;
}
</style>
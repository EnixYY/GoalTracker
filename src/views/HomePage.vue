<template>
    <div id="HomePageHolder">
        <SideNavbar/>
        <WelcomeCard/>
        <OverallGoalsCard/>
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
    flex-direction: column;
}
</style>
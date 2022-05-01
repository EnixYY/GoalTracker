import { createWebHistory, createRouter } from "vue-router";
import HomePage from "@/views/HomePage.vue";
import AssignedGoals from "@/views/AssignedGoals.vue";
import ArchivedGoals from "@/views/ArchivedGoals.vue";
import SignUp from "@/views/SignUp.vue";
import LandingPage from "@/views/LandingPage.vue";
import LoginPage from "@/views/LoginPage.vue";
import CreateGoals from "@/views/CreateGoals.vue";

const routes = [
    {
        path: "/",
        redirect: "/LandingPage",
        name: "index",
        component: LandingPage,
    },
    {
        path: "/LandingPage",
        name: "landingPage",
        component: LandingPage,
    },
    {
        path: "/home",
        name: "home",
        component: HomePage,
    },
    {
        path: "/assignedgoals",
        name: "assignedgoals",
        component: AssignedGoals,
    },
    {
        path: "/archivedgoals",
        name: "archivedgoals",
        component: ArchivedGoals,
    },
    {
        path: "/signUp",
        name: "signUp",
        component: SignUp,
    },
    {
        path: "/login",
        name: "login",
        component: LoginPage,
    },
    {
        path: "/createGoals",
        name: "createGoals",
        component: CreateGoals,
    },
    {
        path: "/logout",
        redirect: "/",
        name: "logout",
        component: LandingPage,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

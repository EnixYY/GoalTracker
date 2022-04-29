import { createWebHistory, createRouter } from "vue-router";
import LandingPage from "@/views/LandingPage.vue";
import AssignedGoals from "@/views/AssignedGoals.vue";
import ArchivedGoals from "@/views/ArchivedGoals.vue";

const routes = [
    {
        path: "/home",
        name: "LandingPage",
        component: LandingPage,
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
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

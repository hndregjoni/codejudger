<template>
<div class="fill-height" style=" display: flex;
  flex-direction: row; ">
  <div >
    <v-container fill-height  >

      <v-card height="100%" width="256">
      <v-navigation-drawer permanent>
        <v-list>
          <role-guard  v-for="item in items" :key="item.title" :roles="item.roles">
            <v-list-item
            
              :key="item.title"
              :to="item.url"
              nuxt
            >
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                {{ item.title }}
              </v-list-item-content>
            </v-list-item>
          </role-guard>
        </v-list>

        <template v-slot:append>
          <div class="pa-2">
            <v-btn block> Logout </v-btn>
          </div>
        </template>
      </v-navigation-drawer>
    </v-card>
    
</v-container>
</div>

    <v-container fill-height fluid >
    
      <NuxtChild />
   
    </v-container>

   
    </div>
 
</template>

<script>
import RoleGuard from '../components/RoleGuard.vue';
export default {
  components: { RoleGuard },

  data() {
    return {
      items: [
        {
          title: "View metrics ",
          icon: "mdi-view-dashboard",
          url: "/settings/metrics",
          roles: ["Admin"]
        },
        {
          title: "Manage profile",
          icon: "mdi-account-box",
          url: "/settings/user",
          roles: ["Admin"],
        },
        {
          title: "Approve requests ",
          icon: "mdi-gavel",
          url: "/settings/requests",
          roles: ["Admin"]
        },
         {
          title: "Tags ",
          icon: "mdi-bookmark-plus",
          url: "/settings/tags",
          roles: ["Admin"]
        },
         {
          title: "Manage languages ",
          icon: "mdi-translate",
          url: "/settings/languages",
          roles: ["Admin"]
        },
         {
          title: "Manage users ",
          icon: "mdi-shimmer",
          url: "/settings/users",
          roles: ["Admin"]
        },
      ],
    };
  },
};
</script>
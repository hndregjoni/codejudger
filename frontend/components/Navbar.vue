 <template>
  <v-app-bar app dense flat color="white">
    <v-container>
      <v-row justify="space-between">
        <v-col>
          <v-menu v-for="text in links" :key="text" offset-y>
            <template v-slot:activator="{ attrs, on }">
              <v-btn text v-bind="attrs" v-on="on">
                {{ text }}
              </v-btn>
            </template>
          </v-menu>
        </v-col>

        <v-col >
            CodeJudger
        </v-col >

        <v-col cols="auto">
          <v-avatar justify-end class="mr-10" color="info" size="32"
            >CJ</v-avatar
          >
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script>
export default {
  data() {
    return {
      links: ["Home", "Problems", "Contest"],
    };
  },
};
</script>

<template >
    <div class=" my-5" >
      <div 
        :class="`rounded-r-xl` "
        class="py-4  text-center primary width:200px "
        
      >
      <label class="white--text" > #Problem 1</label>
      </div>
        <v-spacer></v-spacer>
        <v-row class="justify-center">
            <v-chip class="ma-6 primary" label text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag1
            </v-chip>
                        <v-chip class="ma-6  primary"  label text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag2
            </v-chip>
                        <v-chip class="ma-6  primary" label text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag3
            </v-chip>
                        <v-chip class="ma-6 primary"  label text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag4
            </v-chip>
                        <v-chip class="ma-6 primary"  label text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag5
            </v-chip>
        </v-row>
              <v-textarea
        filled
        outlined
        readonly
        value="Problem statement . . ."
      ></v-textarea>
      <v-btn class="ma-1 primary"  dense flat> Solve </v-btn>
    </div>
</template>

<script>
export default {
    data() {
        return {}
    }
}
</script>

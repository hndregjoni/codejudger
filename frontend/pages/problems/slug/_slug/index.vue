<template >

    <div class=" my-5">
        <v-col cols="12" md="12">
            <div :class="`rounded-r-xl`" class="py-5  text-center primary ">
                <label class="white--text"> #Problem 1</label>
            </div>
        </v-col>
        <v-col align="center" class="justify-center py-6">
            <v-chip class="ma-1 primary"  text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon> 
                Tag1
            </v-chip>
            <v-chip class="ma-1  primary"  text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag2
            </v-chip>
            <v-chip class="ma-1  primary"  text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag3
            </v-chip>
            <v-chip class="ma-1 primary" text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag4
            </v-chip>
            <v-chip class="ma-1 primary" text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag5
            </v-chip>
            
                    <v-col  align="center" cols="12" md="7"> 
            <v-textarea align="center" filled outlined readonly value="Problem statement . . ."></v-textarea>
            <v-btn   class="ma-1 primary" dense flat> Solve </v-btn>
         </v-col>
        </v-col>
 
    </div>
</template>

<script>
export default {
    data() {
        return {

        }
    }
}
</script>
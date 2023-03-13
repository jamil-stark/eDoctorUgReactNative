import { StatusBar } from "expo-status-bar";
import React from "react";
import {
  StyleSheet,
  View,
  Text,
  SafeAreaView,
} from "react-native";
import Home from './Screens/Home';

export default function App() {
  return(
    <View style={styles.container}>
      <Home/>

      {/* {<StatusBar style="auto"  />} */}
    </View>
    
  );


}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    // textAlign: 'center',
    // justifyContent: 'center'
  },


});
import React, { useState, useEffect } from "react";
import { StyleSheet, View, Text, FlatList, Alert } from "react-native";
import { Card, FAB } from "react-native-paper";

function Home() {
  const [data, setData] = useState([{ name: "First Name" }]);

  useEffect(() => {
    fetch("http://192.168.43.28:8000/signup/accounts/", {
       method: "GET" //point to our url of the api with a get method (to get the accounts)
      })
      .then(resp => resp.json()) //receive response then convert it to json. Since it returns a promise.
      .then(data => {
        console.log(data)
      })
      .catch(error => console.log("Error")) //Catch the error and print in the terminal
    
  }, []);
 
  const renderData = (item) => {
    return (
      <Card style={styles.waya}>
        <Text style={{ fontSize: 25 }}>{item.name}</Text>
      </Card>
    );
  };
  return (
    <View>
      <FlatList
        data={data}
        renderItem={({ item }) => {
          return renderData(item);
        }}
        keyExtractor={(item) => item.id}
      />

      <FAB
        style={styles.fab}
        icon="camera"
        onPress={() => console.log("Jamil")}
      />
    </View>
  );
}

export default Home;

const styles = StyleSheet.create({
  waya: {
    padding: 20,
    backgroundColor: "yellow",
    marginTop: 20,
  },

  fab: {
    position: "absolute",
    margin: 16,
    right: 0,
    bottom: 0,
    backgroundColor: "red",
  },
});

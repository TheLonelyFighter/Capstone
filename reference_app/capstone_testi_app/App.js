import React, { useState, useEffect } from 'react';
import { useRoute } from '@react-navigation/native';
import { useLocation } from 'react-router-dom';

import {
  SafeAreaView,
  View,
  Text,
  StyleSheet,
  Image,
  Permissions,
  PermissionsAndroid,
  Platform,
  Button,
  Alert,
} from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { CSVLink, CSVDownload } from 'react-csv';
import Geolocation from 'react-native-geolocation-service';
import GetLocation from 'react-native-get-location';

function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Road Conditions"
        color="blue"
        onPress={() => navigation.navigate('Road Conditions')}
      />
      <Button
        title="Get Coordinates"
        color="green"
        onPress={() => navigation.navigate('Get Coordinates')}
      />
      <Button
        title="Date and Time"
        color="red"
        onPress={() => navigation.navigate('Date and Time')}
      />
    </View>
  );
}

function GetCoordinates({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>getLocation()</Text>
    </View>
  );
}
function GetDates({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>{getCurrentDate()}</Text>
      <Button title="Go back" onPress={() => navigation.goBack()} />
    </View>
  );
}

function DetailsScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Sand on ice"
        color="purple"
        onPress={() => navigation.navigate('Sand On Ice')}
      />
      <Button
        title="Black Ice"
        color="black"
        onPress={() => navigation.navigate('Black Ice')}
      />
      <Button
        title="Ice"
        color="cyan"
        onPress={() => navigation.navigate('Ice')}
      />
      <Button
        title="Wet asphalt"
        color="blue"
        onPress={() => navigation.navigate('Wet Asphalt')}
      />
      <Button
        title="Dry asphalt"
        color="red"
        onPress={() => navigation.navigate('Dry Asphalt')}
      />
      <Button
        title="Sand on asphalt"
        color="brown"
        onPress={() => navigation.navigate('Sand On Asphalt')}
      />
      <Button
        title="Snowy Gravel"
        color="#535AAA"
        onPress={() => navigation.navigate('Snowy Gravel')}
      />
      <Button
        title="Gravel"
        color="#53544E"
        onPress={() => navigation.navigate('Gravel')}
      />
    </View>
  );
}

function BlackIce({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <CSVLink data={csvBlack}>Export as .csv-file</CSVLink>
    </View>
  );
}
function SandOnIce({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <CSVLink data={csvSand}>Export as .csv-file</CSVLink>
    </View>
  );
}
function Ice({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <CSVLink data={csvIce}>Export as .csv-file</CSVLink>
    </View>
  );
}
function DryAsphalt({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <CSVLink data={csvDryAsphalt}>Export as .csv-file</CSVLink>
    </View>
  );
}
function WetAsphalt({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <CSVLink data={csvWetAsphalt}>Export as .csv-file</CSVLink>
    </View>
  );
}
function Gravel({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <CSVLink data={csvGravel}>Export as .csv-file</CSVLink>
    </View>
  );
}
function SandOnAsphalt({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <CSVLink data={csvSandOnAsphalt}>Export as .csv-file</CSVLink>
    </View>
  );
}
function SnowyGravel({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <CSVLink data={csvSnowyGravel}>Export as .csv-file</CSVLink>
    </View>
  );
}

const getLocation = () => {
  return GetLocation.getCurrentPosition({
    enableHighAccuracy: true,
    timeout: 15000,
  })
    .then((location) => {
      console.log(location);
    })
    .catch((error) => {
      const { code, message } = error;
      console.warn(code, message);
    });
};
const getCurrentDate = () => {
  var date = new Date().getDate();
  var month = new Date().getMonth() + 1;
  var year = new Date().getFullYear();
  var hours = new Date().getHours();
  var min = new Date().getMinutes();
  var sec = new Date().getSeconds();
  return date + '-' + month + '-' + year + ' ' + hours + ':' + min + ':' + sec;
};

const Stack = createNativeStackNavigator();

const csvSand = [
  [
    'Date',
    new Date().getDate() +
      '-' +
      (new Date().getMonth() + 1) +
      '-' +
      new Date().getFullYear(),
  ],
  [
    'Time',
    new Date().getHours() +
      ':' +
      new Date().getMinutes() +
      ':' +
      new Date().getSeconds(),
  ],
  ['Coordinates', getLocation()],
  ['Type', 'Sand On Ice'],
];

const csvBlack = [
  [
    'Date',
    new Date().getDate() +
      '-' +
      (new Date().getMonth() + 1) +
      '-' +
      new Date().getFullYear(),
  ],
  [
    'Time',
    new Date().getHours() +
      ':' +
      new Date().getMinutes() +
      ':' +
      new Date().getSeconds(),
  ],
  ['Coordinates', getLocation()],
  ['Type', 'Black Ice'],
];

const csvIce = [
  [
    'Date',
    new Date().getDate() +
      '-' +
      (new Date().getMonth() + 1) +
      '-' +
      new Date().getFullYear(),
  ],
  [
    'Time',
    new Date().getHours() +
      ':' +
      new Date().getMinutes() +
      ':' +
      new Date().getSeconds(),
  ],
  ['Coordinates', getLocation()],
  ['Type', 'Ice'],
];

const csvWetAsphalt = [
  [
    'Date',
    new Date().getDate() +
      '-' +
      (new Date().getMonth() + 1) +
      '-' +
      new Date().getFullYear(),
  ],
  [
    'Time',
    new Date().getHours() +
      ':' +
      new Date().getMinutes() +
      ':' +
      new Date().getSeconds(),
  ],
  ['Coordinates', getLocation()],
  ['Type', 'Wet Asphalt'],
];

const csvDryAsphalt = [
  [
    'Date',
    new Date().getDate() +
      '-' +
      (new Date().getMonth() + 1) +
      '-' +
      new Date().getFullYear(),
  ],
  [
    'Time',
    new Date().getHours() +
      ':' +
      new Date().getMinutes() +
      ':' +
      new Date().getSeconds(),
  ],
  ['Coordinates', getLocation()],
  ['Type', 'Dry Asphalt'],
];

const csvSandOnAsphalt = [
  [
    'Date',
    new Date().getDate() +
      '-' +
      (new Date().getMonth() + 1) +
      '-' +
      new Date().getFullYear(),
  ],
  [
    'Time',
    new Date().getHours() +
      ':' +
      new Date().getMinutes() +
      ':' +
      new Date().getSeconds(),
  ],
  ['Coordinates', getLocation()],
  ['Type', 'Sand On Asphalt'],
];

const csvSnowyGravel = [
  [
    'Date',
    new Date().getDate() +
      '-' +
      (new Date().getMonth() + 1) +
      '-' +
      new Date().getFullYear(),
  ],
  [
    'Time',
    new Date().getHours() +
      ':' +
      new Date().getMinutes() +
      ':' +
      new Date().getSeconds(),
  ],
  ['Coordinates', getLocation()],
  ['Type', 'Snowy Gravel'],
];

const csvGravel = [
  [
    'Date',
    new Date().getDate() +
      '-' +
      (new Date().getMonth() + 1) +
      '-' +
      new Date().getFullYear(),
  ],
  [
    'Time',
    new Date().getHours() +
      ':' +
      new Date().getMinutes() +
      ':' +
      new Date().getSeconds(),
  ],
  ['Coordinates', getLocation()],
  ['Type', 'Gravel'],
];

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Capstone">
        <Stack.Screen name="Capstone" component={HomeScreen} />
        <Stack.Screen name="Road Conditions" component={DetailsScreen} />
        <Stack.Screen name="Get Coordinates" component={GetCoordinates} />
        <Stack.Screen name="Date and Time" component={GetDates} />
        <Stack.Screen name="Sand On Ice" component={SandOnIce} />
        <Stack.Screen name="Black Ice" component={BlackIce} />
        <Stack.Screen name="Ice" component={Ice} />
        <Stack.Screen name="Wet Asphalt" component={WetAsphalt} />
        <Stack.Screen name="Dry Asphalt" component={DryAsphalt} />
        <Stack.Screen name="Sand On Asphalt" component={SandOnAsphalt} />
        <Stack.Screen name="Snowy Gravel" component={SnowyGravel} />
        <Stack.Screen name="Gravel" component={Gravel} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;

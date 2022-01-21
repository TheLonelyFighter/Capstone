import React, { useState, useEffect } from 'react';
import { useRoute } from '@react-navigation/native';
import { useLocation } from 'react-router-dom';
import { useTimer } from 'react-timer-hook';
import DeviceInfo from 'react-native-device-info';

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
  ImageBackground,
} from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { CSVLink, CSVDownload } from 'react-csv';

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
      <Text>{getLocationExpoLocation()}</Text>
    </View>
  );
}
function GetDates({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>{Time()}</Text>
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
    <View style={styles.container}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <ImageBackground
        source={require('./assets/black_ice_cc.jpg')}
        resizeMode="cover"
        style={styles.image}>
        <Text style={styles.text}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Black Ice'],
            ]}
            filename={'start_' + getDateTime() + '_black_ice.csv'}>
            {Time()}
            Start
          </CSVLink>
        </Text>
        <Text style={styles.text_2}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Black Ice'],
            ]}
            filename={'stop_' + getDateTime() + '_black_ice.csv'}>
            {Time()}
            Stop
          </CSVLink>
        </Text>
      </ImageBackground>
    </View>
  );
}
function SandOnIce({ navigation }) {
  return (
    <View style={styles.container}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <ImageBackground
        source={require('./assets/sand_on_ice_cc.jpg')}
        resizeMode="cover"
        style={styles.image}>
        <Text style={styles.text}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Sand On Ice'],
            ]}
            filename={'start_' + getDateTime() + '_sand_on_ice.csv'}>
            {Time()}
            Start
          </CSVLink>
        </Text>
        <Text style={styles.text_2}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Sand On Ice'],
            ]}
            filename={'stop_' + getDateTime() + '_sand_on_ice.csv'}>
            {Time()}
            Stop
          </CSVLink>
        </Text>
      </ImageBackground>
    </View>
  );
}
function Ice({ navigation }) {
  return (
    <View style={styles.container}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <ImageBackground
        source={require('./assets/ice_road_cc.jpg')}
        resizeMode="cover"
        style={styles.image}>
        <Text style={styles.text}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Ice'],
            ]}
            filename={'start_' + getDateTime() + '_ice.csv'}>
            {Time()}
            Start
          </CSVLink>
        </Text>
        <Text style={styles.text_2}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Ice'],
            ]}
            filename={'stop_' + getDateTime() + '_ice.csv'}>
            {Time()}
            Stop
          </CSVLink>
        </Text>
      </ImageBackground>
    </View>
  );
}
function DryAsphalt({ navigation }) {
  return (
    <View style={styles.container}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <ImageBackground
        source={require('./assets/Dry_asphalt_cc.jpg')}
        resizeMode="cover"
        style={styles.image}>
        <Text style={styles.text}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Dry Asphalt'],
            ]}
            filename={'start_' + getDateTime() + '_dry_asphalt.csv'}>
            {Time()}
            Start
          </CSVLink>
        </Text>
        <Text style={styles.text_2}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Dry Asphalt'],
            ]}
            filename={'stop_' + getDateTime() + '_dry_asphalt.csv'}>
            {Time()}
            Stop
          </CSVLink>
        </Text>
      </ImageBackground>
    </View>
  );
}
function WetAsphalt({ navigation }) {
  return (
    <View style={styles.container}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <ImageBackground
        source={require('./assets/wet_asphalt_cc.jpg')}
        resizeMode="cover"
        style={styles.image}>
        <Text style={styles.text}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Wet Asphalt'],
            ]}
            filename={'start_' + getDateTime() + '_wet_asphalt.csv'}>
            {Time()}
            Start
          </CSVLink>
        </Text>
        <Text style={styles.text_2}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Wet Asphalt'],
            ]}
            filename={'stop_' + getDateTime() + '_wet_asphalt.csv'}>
            {Time()}
            Stop
          </CSVLink>
        </Text>
      </ImageBackground>
    </View>
  );
}
function Gravel({ navigation }) {
  return (
    <View style={styles.container}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <ImageBackground
        source={require('./assets/gravel_cc.jpg')}
        resizeMode="cover"
        style={styles.image}>
        <Text style={styles.text}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Gravel'],
            ]}
            filename={'start_' + getDateTime() + '_gravel.csv'}>
            {Time()}
            Start
          </CSVLink>
        </Text>
        <Text style={styles.text_2}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Gravel'],
            ]}
            filename={'stop_' + getDateTime() + '_gravel.csv'}>
            {Time()}
            Stop
          </CSVLink>
        </Text>
      </ImageBackground>
    </View>
  );
}
function SandOnAsphalt({ navigation }) {
  return (
    <View style={styles.container}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <ImageBackground
        source={require('./assets/sand_on_asphalt_cc.jpg')}
        resizeMode="cover"
        style={styles.image}>
        <Text style={styles.text}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Sand On Asphalt'],
            ]}
            filename={'start_' + getDateTime() + '_sand_on_asphalt.csv'}>
            {Time()}
            Start
          </CSVLink>
        </Text>
        <Text style={styles.text_2}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Sand On Asphalt'],
            ]}
            filename={'stop_' + getDateTime() + '_sand_on_asphalt.csv'}>
            {Time()}
            Stop
          </CSVLink>
        </Text>
      </ImageBackground>
    </View>
  );
}
function SnowyGravel({ navigation }) {
  return (
    <View style={styles.container}>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Capstone')}
      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <ImageBackground
        source={require('./assets/snowy_gravel_cc.jpg')}
        resizeMode="cover"
        style={styles.image}>
        <Text style={styles.text}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Snowy Gravel'],
            ]}
            filename={'start_' + getDateTime() + '_snowy_gravel.csv'}>
            {Time()}
            Start
          </CSVLink>
        </Text>
        <Text style={styles.text_2}>
          <CSVLink
            data={[
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
                getHourZeros() +
                  ':' +
                  getMinuteZeros() +
                  ':' +
                  getSecondZeros(),
              ],
              ['Coordinates', getLocationExpoLocation()],
              ['Type', 'Snowy Gravel'],
            ]}
            filename={'stop_' + getDateTime() + '_snowy_gravel.csv'}>
            {Time()}
            Stop
          </CSVLink>
        </Text>
      </ImageBackground>
    </View>
  );
}

function getLocationExpoLocation() {
  const [location, setLocation] = useState(null);
  const [errorMsg, setErrorMsg] = useState(null);

  useEffect(() => {
    (async () => {
      if (Platform.OS === 'android' && !Constants.isDevice) {
        setErrorMsg(
          'Oops, this will not work on Snack in an Android emulator. Try it on your device!'
        );
        return;
      }
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') {
        setErrorMsg('Permission to access location was denied');
        return;
      }

      let location = await Location.getCurrentPositionAsync({});
      setLocation(location);
    })();
  }, []);

  let text = 'Waiting..';
  if (errorMsg) {
    text = errorMsg;
  } else if (location) {
    longitude = JSON.stringify(location.coords.longitude);
    latitude = JSON.stringify(location.coords.latitude);
    speed = JSON.stringify(location.coords.speed);
    text =
      ' Longitude: ' +
      longitude +
      '\n Latitude: ' +
      latitude +
      '\n Speed: ' +
      speed;
  }
  return text;
}

function getDateTime() {
  var now = new Date();
  var year = now.getFullYear();
  var month = now.getMonth() + 1;
  var day = now.getDate();
  var hour = now.getHours();
  var minute = now.getMinutes();
  var second = now.getSeconds();
  if (month.toString().length == 1) {
    month = '0' + month;
  }
  if (day.toString().length == 1) {
    day = '0' + day;
  }
  if (hour.toString().length == 1) {
    hour = '0' + hour;
  }
  if (minute.toString().length == 1) {
    minute = '0' + minute;
  }
  if (second.toString().length == 1) {
    second = '0' + second;
  }
  var dateTime =
    day + '_' + month + '_' + year + '_' + hour + '_' + minute + '_' + second;
  return dateTime;
}

function getHourZeros() {
  var now = new Date();
  var hour = now.getHours();

  if (hour.toString().length == 1) {
    hour = '0' + hour;
  }

  return hour;
}

function getSecondZeros() {
  var now = new Date();
  var sec = now.getSeconds();

  if (sec.toString().length == 1) {
    sec = '0' + sec;
  }

  return sec;
}

function getMinuteZeros() {
  var now = new Date();
  var min = now.getMinutes();

  if (min.toString().length == 1) {
    min = '0' + min;
  }

  return min;
}

function Time() {
  const [time, setTime] = React.useState(new Date());

  React.useEffect(() => {
    setInterval(() => {
      setTime(new Date());
    }, 1000);
  }, []);

  return <span>{time.toLocaleTimeString().split('.').join('_')} </span>;
}

const Stack = createNativeStackNavigator();

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

const styles = StyleSheet.create({
  top: {
    flex: 0.3,
    borderWidth: 5,
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
  },
  container: {
    flex: 1,
  },
  image: {
    flex: 1,
    justifyContent: 'top',
  },
  text: {
    color: 'white',
    fontSize: 25,
    lineHeight: 80,
    fontWeight: 'bold',
    textAlign: 'center',
    backgroundColor: 'white',
  },
  text_2: {
    color: 'white',
    fontSize: 25,
    lineHeight: 80,
    fontWeight: 'bold',
    textAlign: 'center',
    backgroundColor: 'red',
  },
});

export default App;

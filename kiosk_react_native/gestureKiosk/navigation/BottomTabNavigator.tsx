import { Ionicons } from '@expo/vector-icons';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import * as React from 'react';

import Colors from '../constants/Colors';
import useColorScheme from '../hooks/useColorScheme';
import Movies from '../screens/Movies';
import Seats from '../screens/Seats';
import Checkout from '../screens/Checkout';
import { BottomTabParamList, CheckoutParamList, MoviesParamList, SeatsParamList } from '../types';

const BottomTab = createBottomTabNavigator<BottomTabParamList>();

export default function BottomProgressTabs() {
  const colorScheme = useColorScheme();

  /**
   * TODO: BOTTOM NAVIGATOR NEEDS TO BE A PROGRESS BAR BASED ON THE SELECTED TAB
   * 
   * TABS WILL BE movies -> seats -> checkout
   */
  return (
            // bottom screen navigation movies tabs
    <BottomTab.Navigator
      initialRouteName="Movies"
      tabBarOptions={{ activeTintColor: Colors[colorScheme].tint }}>
      <BottomTab.Screen
        name="Movies"
        component={MovieNavigator}
        options={{
          tabBarIcon: ({ color }) => <TabBarIcon name="ios-code" color={color} />,
        }}
      />
              // bottom screen navigation seats tabs
      <BottomTab.Screen
        name="Seats"
        component={SeatsNavigator}
        options={{
          tabBarIcon: ({ color }) => <TabBarIcon name="ios-code" color={color} />,
        }}
        // bottom screen navigation checkout tabs
      />
          <BottomTab.Screen
          name="Checkout"
          component={CheckoutNavigator}
          options={{
            tabBarIcon: ({ color }) => <TabBarIcon name="ios-code" color={color} />,
          }}
        />
      </BottomTab.Navigator>
  );
}

// You can explore the built-in icon families and icons on the web at:
// https://icons.expo.fyi/
function TabBarIcon(props: { name: React.ComponentProps<typeof Ionicons>['name']; color: string }) {
  return <Ionicons size={30} style={{ marginBottom: -3 }} {...props} />;
}

// Each tab has its own navigation stack, you can read more about this pattern here:
// https://reactnavigation.org/docs/tab-based-navigation#a-stack-navigator-for-each-tab
const MoviesStack = createStackNavigator<MoviesParamList>();

function MovieNavigator() {
  return (
    <MoviesStack.Navigator>
      <MoviesStack.Screen
        name="MoviesScreen"
        component={Movies}
        options={{ headerTitle: 'Please select a movie...' }}
      />
    </MoviesStack.Navigator>
  );
}


//navigator for seat stack state stored memory

const SeatsStack = createStackNavigator<SeatsParamList>();

function SeatsNavigator() {
  return (
    <SeatsStack.Navigator>
      <SeatsStack.Screen
        name="SeatsScreen"
        component={Seats}
        options={{ headerTitle: 'Please select a seat...' }}
      />
    </SeatsStack.Navigator>
  );
}

const CheckoutStack = createStackNavigator<CheckoutParamList>();


//navigator for checkout param list
function CheckoutNavigator() {
  return (
    <CheckoutStack.Navigator>
      <CheckoutStack.Screen
        name="CheckoutScreen"
        component={Checkout}
        options={{ headerTitle: 'Please enter your payment information.' }}
      />
    </CheckoutStack.Navigator>
  );
}

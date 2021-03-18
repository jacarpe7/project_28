import * as Linking from 'expo-linking';

/**
 * Creates URL's for router
 */
export default {
  prefixes: [Linking.makeUrl('/')],
  config: {
    screens: {
      Root: {
        screens: {
          Movies: {
            screens: {
              MoviesScreen: 'one',
            },
          },
          Seats: {
            screens: {
              SeatsScreen: 'two',
            },
          },
          Checkout: {
            screens: {
              CheckoutScreen: 'three',
            },
          },
        },
      },
      NotFound: '*',
    },
  },
};

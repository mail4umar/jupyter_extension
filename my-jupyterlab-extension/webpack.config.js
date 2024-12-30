const path = require('path');

module.exports = {
  entry: './src/index.ts', // Specify the entry file
  output: {
    filename: 'index.js', // Change this to match your expected output file
    path: path.resolve(__dirname, 'lib'),
  },
  resolve: {
    extensions: ['.ts', '.js'], // Resolve .ts and .js files
  },
  module: {
    rules: [
      {
        test: /\.ts$/, // Process .ts files
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.svg$/,
        use: [
          {
            loader: 'svg-url-loader',
            options: {
              limit: 8192, // Convert SVG files to data URLs if they are smaller than 8KB
            },
          },
        ],
      },
    ],
  },
  mode: 'development', // Set to 'development' for now
};

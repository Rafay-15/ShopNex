# Use an official Node.js image as a base image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 3000 (React default port for development server)
EXPOSE 3000

# Run the React development server
CMD ["npm", "start"]


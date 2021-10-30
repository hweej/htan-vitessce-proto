
// Todo
// Add proptypes
// Define defaults args
// Add various ways to alter style

const Button = ({label, children}) => {
  return (
    <button class="py-2 px-3 bg-blue-500 text-white rounded-lg">
    {children}
      </button>
  )
}

export default Button;

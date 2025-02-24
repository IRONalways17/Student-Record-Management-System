// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
       // Handle search functionality
       const searchInput = document.getElementById('searchInput');
       if (searchInput) {
           searchInput.addEventListener('input', debounce(handleSearch, 300));
       }
   
       // Auto-hide alerts after 5 seconds
       const alerts = document.querySelectorAll('.alert');
       alerts.forEach(alert => {
           setTimeout(() => {
               const bsAlert = new bootstrap.Alert(alert);
               bsAlert.close();
           }, 5000);
       });
   });
   
   // Debounce function to limit API calls
   function debounce(func, wait) {
       let timeout;
       return function executedFunction(...args) {
           const later = () => {
               clearTimeout(timeout);
               func(...args);
           };
           clearTimeout(timeout);
           timeout = setTimeout(later, wait);
       };
   }
   
   // Handle search functionality
   function handleSearch(e) {
       const searchQuery = e.target.value.trim();
       const tbody = document.getElementById('studentTableBody');
   
       if (searchQuery.length === 0) {
           // Reload the page to show all records
           window.location.reload();
           return;
       }
   
       // Make API call to search endpoint
       fetch(`/search?query=${encodeURIComponent(searchQuery)}`)
           .then(response => response.json())
           .then(students => {
               tbody.innerHTML = ''; // Clear current table
   
               if (students.length === 0) {
                   const tr = document.createElement('tr');
                   tr.innerHTML = `
                       <td colspan="6" class="text-center">
                           No students found matching "${searchQuery}"
                       </td>
                   `;
                   tbody.appendChild(tr);
                   return;
               }
   
               students.forEach(student => {
                   const tr = document.createElement('tr');
                   tr.innerHTML = `
                       <td>${student.roll_number}</td>
                       <td>${student.name}</td>
                       <td>${student.email}</td>
                       <td>${student.grade}</td>
                       <td>${student.created_by || 'N/A'}</td>
                       <td>
                           <a href="/edit_student/${student.id}" class="btn btn-sm btn-warning">
                               <i class="bi bi-pencil-fill"></i> Edit
                           </a>
                           <a href="/delete_student/${student.id}" 
                              class="btn btn-sm btn-danger"
                              onclick="return confirm('Are you sure you want to delete this student?')">
                               <i class="bi bi-trash-fill"></i> Delete
                           </a>
                       </td>
                   `;
                   tbody.appendChild(tr);
               });
           })
           .catch(error => {
               console.error('Error:', error);
               showError('An error occurred while searching. Please try again.');
           });
   }
   
   // Show error message
   function showError(message) {
       const alertDiv = document.createElement('div');
       alertDiv.className = 'alert alert-danger alert-dismissible fade show';
       alertDiv.innerHTML = `
           ${message}
           <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
       `;
       document.querySelector('.container').insertBefore(
           alertDiv,
           document.querySelector('.container').firstChild
       );
   }
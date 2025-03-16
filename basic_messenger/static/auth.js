// Общие функции
const API_BASE = window.location.origin + '/api/';

// Обработчик регистрации
if (document.getElementById('registerForm')) {
	document.getElementById('registerForm').addEventListener('submit', async (e) => {
		e.preventDefault();
		const data = {
			username: document.getElementById('username').value,
			password: document.getElementById('password').value,
			name: document.getElementById('name').value
		};

		try {
			const response = await fetch(API_BASE + 'register/', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify(data)
			});

			if (response.ok) {
				window.location.href = '/login/'; // Перенаправление на вход
			} else {
				const errorData = await response.json();
				showError(errorData);
			}
		} catch (err) {
			showError({ detail: 'Ошибка соединения' });
		}
	});
}

// Обработчик входа
if (document.getElementById('loginForm')) {
	document.getElementById('loginForm').addEventListener('submit', async (e) => {
		e.preventDefault();
		const data = {
			username: document.getElementById('username').value,
			password: document.getElementById('password').value
		};

		try {
			const response = await fetch(API_BASE + 'token/', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify(data)
			});

			if (response.ok) {
				const tokens = await response.json();
				localStorage.setItem('access_token', tokens.access);
				localStorage.setItem('refresh_token', tokens.refresh);
				console.log(tokens.access, tokens.refresh);
				window.location.href = '/'; // Перенаправление на главную
			} else {
				const errorData = await response.json();
				showError(errorData);
			}
		} catch (err) {
			showError({ detail: 'Ошибка соединения' });
		}
	});
}



// Показать ошибку
function showError(error) {
	const errorDiv = document.getElementById('error');
	errorDiv.textContent = error.detail || 'Неизвестная ошибка';
}
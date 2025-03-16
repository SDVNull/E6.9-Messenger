const API_BASE = window.location.origin + '/api/';

// Обработчик работы с профилем
if (document.getElementById('profileForm')) {
	document.getElementById('profileForm').addEventListener('submit', async (e) => {
		e.preventDefault();
		const data = {
			name: document.getElementById('name').value,
			avatar: document.getElementById('avatar').files[0]
		};

		try {
			const formData = new FormData();
			formData.append('name', data.name);
			if (data.avatar) {
				formData.append('avatar', data.avatar);
			}

			const response = await fetch(API_BASE + 'profile/', {
				method: 'POST',
				headers: {
					'Authorization': `Bearer ${localStorage.getItem('access_token')}`
				},
				body: formData
			});

			if (response.ok) {
				alert('Профиль успешно обновлен!');
			} else {
				const errorData = await response.json();
				showError(errorData);
			}
		} catch (err) {
			showError({ detail: 'Ошибка соединения' });
		}
	});
}
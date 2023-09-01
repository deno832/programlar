using Mesajlaşma_Api1.Data;
using Mesajlaşma_Api1.Models.Domain;
using Mesajlaşma_Api1.Models.DTO;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace Mesajlaşma_Api1.Controllers
{
	[Route("api/[controller]")]
	[ApiController]
	public class UsersController : ControllerBase
	{
		private readonly Mesajlaşma_Api1DbContext dbContext;
		public UsersController(Mesajlaşma_Api1DbContext dbContext)
		{
			this.dbContext = dbContext;
		}

		[HttpPost]
		[Route("register")]
		public IActionResult Register([FromBody] AddUserDto addUserDto)
		{
			var User_domain_model = new User
			{
				Nickname = addUserDto.Nickname,
				Password = addUserDto.Password,
				MailAddress = addUserDto.MailAddress,
			};

			dbContext.Users.Add(User_domain_model);
			dbContext.SaveChanges();

			return Ok("Yaptm aga");
		}

		[HttpGet]
		[Route("get_users_id/{name}")]
		public IActionResult Bisi(string name)
		{
			var result = dbContext.Users.FirstOrDefault(x => x.Nickname == name);

			if (result == null)
			{
				return NotFound();
			}

			return Ok(result);
		}

		[HttpPost]
		[Route("login")]
		public IActionResult Login([FromBody] LoginDto loginDto)
		{
			var user = dbContext.Users.FirstOrDefault(u => u.Nickname == loginDto.Nickname && u.Password == loginDto.Password);
			
			if (user != null)
			{
				var sucess = new
				{
					message = "Succesfull login!",
					id = user.Id,
				};

				return Ok(sucess);
			}
			
			var response = new
			{
				message = "Invalid Credentials"
			};

			return NotFound(response);
		}
	}
}
